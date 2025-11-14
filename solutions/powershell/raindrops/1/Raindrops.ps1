function Get-Raindrops {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [int]$Rain
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        $result = ""

        if ($Rain % 3 -eq 0) { $result += "Pling" }
        if ($Rain % 5 -eq 0) { $result += "Plang" }
        if ($Rain % 7 -eq 0) { $result += "Plong" }

        if ([string]::IsNullOrEmpty($result)) {
            return "$Rain"
        } else {
            return $result
        }
    }
}
