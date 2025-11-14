function Get-NucleotideCount {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyString()]
        [string]$Strand
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        # Initialize counts
        $counts = @{
            A = 0
            C = 0
            G = 0
            T = 0
        }

        foreach ($ch in $Strand.ToCharArray()) {
            $k = ([string]$ch).ToUpperInvariant()
            if ($counts.ContainsKey($k)) {
                $counts[$k]++
            } else {
                throw "Invalid nucleotide in strand: '$ch'"
            }
        }

        return $counts
    }
}
