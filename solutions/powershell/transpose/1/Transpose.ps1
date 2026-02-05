function Invoke-Transpose {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string] $Text
    )

    if ([string]::IsNullOrEmpty($Text)) {
        return ""
    }

    # Force array output even when there's only one line
    $lines = @(
        $Text -split "`n" |
            ForEach-Object { $_ -replace "`r$", "" }
    )

    $maxLen = 0
    foreach ($line in $lines) {
        if ($line.Length -gt $maxLen) { $maxLen = $line.Length }
    }

    $outLines = New-Object System.Collections.Generic.List[string]

    for ($col = 0; $col -lt $maxLen; $col++) {

        # Find the last row that actually has a character at this column
        $lastRow = -1
        for ($row = $lines.Length - 1; $row -ge 0; $row--) {
            if ($col -lt $lines[$row].Length) {
                $lastRow = $row
                break
            }
        }

        if ($lastRow -lt 0) { continue }

        $chars = New-Object 'System.Collections.Generic.List[char]'
        for ($row = 0; $row -le $lastRow; $row++) {
            if ($col -lt $lines[$row].Length) {
                $chars.Add($lines[$row][$col])
            } else {
                $chars.Add(' ')
            }
        }

        $outLines.Add((-join $chars))
    }

    return ($outLines -join "`n")
}
