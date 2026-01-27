function Get-Proverb {
    [CmdletBinding()]
    param(
        [Parameter()]
        [string[]]$Data = @()
    )

    if ($null -eq $Data -or $Data.Count -eq 0) {
        return ""
    }

    $lines = @()

    for ($i = 0; $i -lt $Data.Count - 1; $i++) {
        $lines += "For want of a $($Data[$i]) the $($Data[$i + 1]) was lost."
    }

    $lines += "And all for the want of a $($Data[0])."

    $lines -join "`r`n"
}
