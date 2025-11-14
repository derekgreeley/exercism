Enum Triangle {
    EQUILATERAL
    ISOSCELES
    SCALENE
}

function Get-Triangle {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [double[]]$Sides
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        if ($Sides.Count -ne 3) {
            throw "Exactly three side lengths are required."
        }

        $a, $b, $c = $Sides

        # --- Validation: positive sides ---
        if ($a -le 0 -or $b -le 0 -or $c -le 0) {
            throw "All side lengths must be positive."
        }

        # --- Triangle inequality (allow degenerate: use <, not <=) ---
        if ( ($a + $b) -lt $c -or
             ($b + $c) -lt $a -or
             ($a + $c) -lt $b ) {
            throw "Side lengths violate triangle inequality."
        }

        # --- Classification ---
        $eqAB = ($a -eq $b)
        $eqBC = ($b -eq $c)
        $eqAC = ($a -eq $c)

        if ($eqAB -and $eqBC) {
            return [Triangle]::EQUILATERAL
        }
        elseif ($eqAB -or $eqBC -or $eqAC) {
            return [Triangle]::ISOSCELES
        }
        else {
            return [Triangle]::SCALENE
        }
    }
}
