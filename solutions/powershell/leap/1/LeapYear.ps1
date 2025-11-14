function Test-LeapYear {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [int]$Year
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        # Leap year if divisible by 400
        if ($Year % 400 -eq 0) { return $true }

        # Not a leap year if divisible by 100
        if ($Year % 100 -eq 0) { return $false }

        # Leap year if divisible by 4
        if ($Year % 4 -eq 0) { return $true }

        # Otherwise not a leap year
        return $false
    }
}
