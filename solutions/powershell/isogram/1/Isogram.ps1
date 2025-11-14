function Invoke-Isogram {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyString()]
        [string]$Phrase
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        if ($Phrase.Length -eq 0) { return $true }  # empty string is an isogram

        # Case-insensitive; consider only letters; ignore spaces, hyphens, punctuation.
        $seen = [System.Collections.Generic.HashSet[char]]::new()
        foreach ($ch in $Phrase.ToLowerInvariant().ToCharArray()) {
            if ($ch -ge 'a' -and $ch -le 'z') {
                if (-not $seen.Add($ch)) {
                    return $false   # duplicate letter found
                }
            }
        }
        return $true
    }
}