function Test-MatchingBrackets {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string] $InputString
    )

    # Map closing -> opening
    $pairs = @{
        ')' = '('
        ']' = '['
        '}' = '{'
    }

    # Use a real stack
    $stack = New-Object 'System.Collections.Generic.Stack[char]'

    foreach ($ch in $InputString.ToCharArray()) {
        switch ($ch) {
            '(' { $stack.Push($ch); continue }
            '[' { $stack.Push($ch); continue }
            '{' { $stack.Push($ch); continue }

            ')' {
                if ($stack.Count -eq 0) { return $false }
                if ($stack.Pop() -ne $pairs[')']) { return $false }
                continue
            }
            ']' {
                if ($stack.Count -eq 0) { return $false }
                if ($stack.Pop() -ne $pairs[']']) { return $false }
                continue
            }
            '}' {
                if ($stack.Count -eq 0) { return $false }
                if ($stack.Pop() -ne $pairs['}']) { return $false }
                continue
            }
            default { continue } # ignore everything else
        }
    }

    return ($stack.Count -eq 0)
}
