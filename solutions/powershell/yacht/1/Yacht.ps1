# Yacht.ps1

Set-StrictMode -Version Latest

enum Category {
    YACHT
    ONES
    TWOS
    THREES
    FOURS
    FIVES
    SIXES
    FULL_HOUSE
    FOUR_OF_A_KIND
    LITTLE_STRAIGHT
    BIG_STRAIGHT
    CHOICE
}

function Get-Score {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position = 0)]
        [int[]] $Dice,

        [Parameter(Mandatory, Position = 1)]
        [Category] $Category
    )

    # Frequency map for the five dice
    $counts = @{}
    foreach ($d in $Dice) {
        if ($counts.ContainsKey($d)) {
            $counts[$d]++
        } else {
            $counts[$d] = 1
        }
    }

    switch ($Category) {

        'YACHT' {
            if ($counts.Count -eq 1 -and $Dice.Count -eq 5 -and ($counts.Values | Select-Object -First 1) -eq 5) {
                return 50
            }
            return 0
        }

        'ONES' {
            return ($Dice | Where-Object { $_ -eq 1 } | Measure-Object -Sum).Sum
        }

        'TWOS' {
            $cnt = ($Dice | Where-Object { $_ -eq 2 } | Measure-Object).Count
            return 2 * $cnt
        }

        'THREES' {
            $cnt = ($Dice | Where-Object { $_ -eq 3 } | Measure-Object).Count
            return 3 * $cnt
        }

        'FOURS' {
            $cnt = ($Dice | Where-Object { $_ -eq 4 } | Measure-Object).Count
            return 4 * $cnt
        }

        'FIVES' {
            $cnt = ($Dice | Where-Object { $_ -eq 5 } | Measure-Object).Count
            return 5 * $cnt
        }

        'SIXES' {
            $cnt = ($Dice | Where-Object { $_ -eq 6 } | Measure-Object).Count
            return 6 * $cnt
        }

        'FULL_HOUSE' {
            if ($counts.Count -ne 2) { return 0 }

            $vals = $counts.Values
            if ($vals -contains 3 -and $vals -contains 2) {
                return ($Dice | Measure-Object -Sum).Sum
            }
            return 0
        }

        'FOUR_OF_A_KIND' {
            foreach ($key in $counts.Keys) {
                if ($counts[$key] -ge 4) {
                    return 4 * [int]$key
                }
            }
            return 0
        }

        'LITTLE_STRAIGHT' {
            $sorted = $Dice | Sort-Object
            # sequence equality: no differences from 1..5
            if (-not (Compare-Object $sorted (1,2,3,4,5))) {
                return 30
            }
            return 0
        }

        'BIG_STRAIGHT' {
            $sorted = $Dice | Sort-Object
            if (-not (Compare-Object $sorted (2,3,4,5,6))) {
                return 30
            }
            return 0
        }

        'CHOICE' {
            return ($Dice | Measure-Object -Sum).Sum
        }
    }
}
