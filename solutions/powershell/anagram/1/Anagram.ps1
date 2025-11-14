function Invoke-Anagram {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Subject,

        [Parameter(Mandatory)]
        [string[]]$Candidates
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'

        function Get-Signature {
            param([string]$s)
            # Normalize & case-fold, then sort characters ordinally to build a multiset signature
            $norm = $s.Normalize([Text.NormalizationForm]::FormC).ToLowerInvariant()
            $chars = $norm.ToCharArray()
            [Array]::Sort($chars)     # ordinal sort on Unicode code points
            -join $chars
        }

        $subjectLower = $Subject.Normalize([Text.NormalizationForm]::FormC).ToLowerInvariant()
        $subjectSig   = Get-Signature $Subject
        $subjectLen   = $Subject.Length
    }

    process {
        $result = New-Object System.Collections.Generic.List[string]

        foreach ($cand in $Candidates) {
            if ([string]::IsNullOrEmpty($cand)) { continue }

            # Exclude the same word (case-insensitive)
            $candLower = $cand.Normalize([Text.NormalizationForm]::FormC).ToLowerInvariant()
            if ($candLower -eq $subjectLower) { continue }

            # Quick length check (prevents subset/duplicate-letter false positives)
            if ($cand.Length -ne $subjectLen) { continue }

            # Compare multiset signatures
            if ((Get-Signature $cand) -eq $subjectSig) {
                [void]$result.Add($cand)  # keep original casing/order
            }
        }

        ,$result.ToArray()
    }
}
