function Get-LetterFrequencies {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyCollection()]
        [string[]]$Texts
    )

    $result = @{}

    foreach ($text in $Texts) {
        if ($null -eq $text) {
            continue
        }

        foreach ($match in [regex]::Matches($text.ToLowerInvariant(), '\p{L}')) {
            $letter = $match.Value
            if ($result.ContainsKey($letter)) {
                $result[$letter]++
            }
            else {
                $result[$letter] = 1
            }
        }
    }

    return $result
}