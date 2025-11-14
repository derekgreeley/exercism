function Get-Answer {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [string]$Question
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        if ([string]::IsNullOrWhiteSpace($Question)) { throw "Unknown operation" }

        # Allow empty expression before '?', so we can classify as Syntax Error later
        $m = [regex]::Match($Question, '^\s*What\s+is\s*(.*)\?\s*$')
        if (-not $m.Success) { throw "Unknown operation" }

        $expr = $m.Groups[1].Value.Trim()

        # Empty after "What is" -> Syntax Error
        if ([string]::IsNullOrWhiteSpace($expr)) { throw "Syntax Error" }

        # Normalize multi-word ops
        $expr = $expr -replace '\bmultiplied\s+by\b', 'multiplied_by'
        $expr = $expr -replace '\bdivided\s+by\b', 'divided_by'

        $tokens = $expr -split '\s+'
        if ($tokens.Count -eq 0) { throw "Syntax Error" }

        $validOps = @('plus','minus','multiplied_by','divided_by')

        $expectNumber = $true
        $haveFirst    = $false
        [int]$result  = 0
        $currentOp    = $null

        for ($i = 0; $i -lt $tokens.Count; $i++) {
            $t = $tokens[$i]

            if ($expectNumber) {
                # Expect a number
                [int]$n = 0
                if (-not [int]::TryParse($t, [ref]$n)) {
                    # If we got an operator here -> syntax error
                    if ($validOps -contains $t) { throw "Syntax Error" }
                    # Unknown word when number expected
                    throw "Unknown operation"
                }

                if (-not $haveFirst) {
                    $result    = $n
                    $haveFirst = $true
                } else {
                    switch ($currentOp) {
                        'plus'          { $result = $result + $n }
                        'minus'         { $result = $result - $n }
                        'multiplied_by' { $result = $result * $n }
                        'divided_by'    { $result = [int]($result / $n) }
                        default         { throw "Syntax Error" }
                    }
                }
                $expectNumber = $false
            }
            else {
                # Expect an operator
                # If we see a number where an operator should be -> Syntax Error (two numbers in a row / postfix)
                [int]$dummy = 0
                if ([int]::TryParse($t, [ref]$dummy)) { throw "Syntax Error" }

                if ($validOps -notcontains $t) {
                    throw "Unknown operation"
                }
                $currentOp    = $t
                $expectNumber = $true
            }
        }

        if ($expectNumber) { throw "Syntax Error" }  # expression ends with operator

        return $result
    }
}
