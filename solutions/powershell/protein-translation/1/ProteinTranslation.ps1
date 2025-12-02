function Invoke-ProteinTranslation {
    [CmdletBinding()]
    param(
        [string]$Strand
    )

    # Map codons to amino acids
    $codonMap = @{
        'AUG' = 'Methionine'

        'UUU' = 'Phenylalanine'
        'UUC' = 'Phenylalanine'

        'UUA' = 'Leucine'
        'UUG' = 'Leucine'

        'UCU' = 'Serine'
        'UCC' = 'Serine'
        'UCA' = 'Serine'
        'UCG' = 'Serine'

        'UAU' = 'Tyrosine'
        'UAC' = 'Tyrosine'

        'UGU' = 'Cysteine'
        'UGC' = 'Cysteine'

        'UGG' = 'Tryptophan'
    }

    $stopCodons = @('UAA', 'UAG', 'UGA')

    # Empty strand → no proteins
    if ([string]::IsNullOrEmpty($Strand)) {
        return @()
    }

    $proteins = New-Object System.Collections.Generic.List[string]

    $i = 0
    while ($i -lt $Strand.Length) {

        # Not enough bases for a full codon -> invalid
        if ($i + 3 -gt $Strand.Length) {
            throw "error: Invalid codon"
        }

        $codon = $Strand.Substring($i, 3)

        # STOP codon → halt processing
        if ($stopCodons -contains $codon) {
            break
        }

        # Unknown codon -> error
        if (-not $codonMap.ContainsKey($codon)) {
            throw "error: Invalid codon"
        }

        # Add translated protein
        $proteins.Add($codonMap[$codon]) | Out-Null

        $i += 3
    }

    return $proteins.ToArray()
}
