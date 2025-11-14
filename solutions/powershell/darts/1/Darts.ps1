function Invoke-Darts {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [double]$X,

        [Parameter(Mandatory, Position=1)]
        [double]$Y
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        # Use squared distance to avoid sqrt
        $r2 = ($X * $X) + ($Y * $Y)

        if     ($r2 -le 1)   { return 10 }  # radius <= 1
        elseif ($r2 -le 25)  { return 5 }   # radius <= 5
        elseif ($r2 -le 100) { return 1 }   # radius <= 10
        else                  { return 0 }
    }
}
