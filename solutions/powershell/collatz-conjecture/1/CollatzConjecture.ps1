function Invoke-CollatzConjecture {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [long]$Number
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        if ($Number -le 0) {
            throw "error: Only positive numbers are allowed"
        }

        if ($Number -eq 1) { return 0 }

        [long]$n = $Number
        [int]$steps = 0

        while ($n -ne 1) {
            if (($n % 2) -eq 0) {
                $n = [long]($n / 2)
            } else {
                $n = [long](3 * $n + 1)
            }
            $steps++
        }

        return $steps
    }
}
