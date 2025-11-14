function Invoke-Panagram {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyString()]
        [string]$Sentence
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'

        # Precompute the full a–z set once
        $allLetters = [System.Collections.Generic.HashSet[char]]::new(
            [char[]]('a'..'z')
        )
    }

    process {
        if ([string]::IsNullOrEmpty($Sentence)) { return $false }

        # Track which letters we’ve seen
        $seen = [System.Collections.Generic.HashSet[char]]::new()
        foreach ($ch in $Sentence.ToLowerInvariant().ToCharArray()) {
            if ($ch -ge 'a' -and $ch -le 'z') {
                [void]$seen.Add($ch)
                if ($seen.Count -eq 26) { return $true } # early exit
            }
        }

        return ($seen.Count -eq 26)
    }
}