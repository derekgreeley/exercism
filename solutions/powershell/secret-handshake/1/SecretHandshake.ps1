function Invoke-SecretHandshake {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [int]$Number
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        $actions = @()

        # Check each bit position (1–16)
        if ($Number -band 1)     { $actions += "wink" }
        if ($Number -band 2)     { $actions += "double blink" }
        if ($Number -band 4)     { $actions += "close your eyes" }
        if ($Number -band 8)     { $actions += "jump" }

        # If 5th bit (16) is set → reverse order
        if ($Number -band 16) {
            [array]::Reverse($actions)
        }

         return ,$actions  # ensure an array is always returned
    }
}

