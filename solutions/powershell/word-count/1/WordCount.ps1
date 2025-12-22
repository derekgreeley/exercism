# WordCount.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Get-WordCount {
    [CmdletBinding()]
    param(
        # Must allow empty string (some tracks include it); treat as no words
        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Phrase
    )

    $counts = @{}

    if ([string]::IsNullOrEmpty($Phrase)) {
        return $counts
    }

    # Match "words" as:
    # - one or more alphanumerics
    # - with optional internal apostrophe groups for contractions (e.g., can't, you're)
    # Apostrophes at the edges are ignored because they won't be part of a match.
    $matches = [regex]::Matches($Phrase.ToLowerInvariant(), "[a-z0-9]+(?:'[a-z0-9]+)*")

    foreach ($m in $matches) {
        $w = $m.Value
        if ($counts.ContainsKey($w)) {
            $counts[$w]++
        } else {
            $counts[$w] = 1
        }
    }

    return $counts
}
