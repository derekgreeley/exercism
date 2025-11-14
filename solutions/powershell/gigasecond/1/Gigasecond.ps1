function Add-Gigasecond {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [datetime]$Time
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
        # Use an exact integer count of seconds to avoid rounding issues
        $Gigaseconds = 1000000000 # 1e9
    }

    process {
        # Add exactly 1,000,000,000 seconds; preserves DateTime Kind (Local/UTC)
        return $Time.AddSeconds($Gigaseconds)
    }
}