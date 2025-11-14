function Invoke-RnaTranscription {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyString()]
        [string]$Strand
    )

    process {
        if ($Strand.Length -eq 0) { return "" }

        $map = @{
            'G' = 'C'
            'C' = 'G'
            'T' = 'A'
            'A' = 'U'
        }

        $sb = [System.Text.StringBuilder]::new()

        foreach ($ch in $Strand.ToCharArray()) {
            $k = ([string]$ch).ToUpperInvariant()  # ensure string key
            if (-not $map.ContainsKey($k)) {
                throw "Invalid nucleotide '$ch'"
            }
            [void]$sb.Append($map[$k])
        }

        $sb.ToString()
    }
}
