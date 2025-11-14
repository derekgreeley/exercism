function Get-HammingDifference {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyString()]
        [string]$Strand1,

        [Parameter(Mandatory, Position=1)]
        [AllowEmptyString()]
        [string]$Strand2
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        # Validate equal length
        if ($Strand1.Length -ne $Strand2.Length) {
            throw "DNA strands must be of equal length."
        }

        # Empty strands → distance = 0
        if ($Strand1.Length -eq 0) {
            return 0
        }

        $distance = 0
        for ($i = 0; $i -lt $Strand1.Length; $i++) {
            if ($Strand1[$i] -ne $Strand2[$i]) {
                $distance++
            }
        }

        return $distance
    }
}

