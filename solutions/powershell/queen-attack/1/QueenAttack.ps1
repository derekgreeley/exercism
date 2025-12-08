# QueenAttack.ps1

Set-StrictMode -Version Latest

class ChessBoard {
    [int[]]$White
    [int[]]$Black

    ChessBoard() {
        # Default starting positions:
        # White at (7,3), Black at (0,3)
        $this.Init(@(7, 3), @(0, 3))
    }

    ChessBoard([int[]]$White, [int[]]$Black) {
        $this.Init($White, $Black)
    }

    hidden [void]Init([int[]]$white, [int[]]$black) {
        if ($null -eq $white -or $white.Count -ne 2) {
            throw "White queen must be placed on the board"
        }
        if ($null -eq $black -or $black.Count -ne 2) {
            throw "Black queen must be placed on the board"
        }

        $this.ValidatePosition($white, "White")
        $this.ValidatePosition($black, "Black")

        # Queens cannot share same square
        if ($white[0] -eq $black[0] -and $white[1] -eq $black[1]) {
            throw "Queens can not share the same space"
        }

        $this.White = $white
        $this.Black = $black
    }

    hidden [void]ValidatePosition([int[]]$pos, [string]$color) {
        $row = $pos[0]
        $col = $pos[1]

        if ($row -lt 0 -or $row -gt 7 -or $col -lt 0 -or $col -gt 7) {
            throw "$color queen must be placed on the board"
        }
    }

    [bool]CanAttack() {
        $wr = $this.White[0]
        $wc = $this.White[1]
        $br = $this.Black[0]
        $bc = $this.Black[1]

        # Same row or same column
        if ($wr -eq $br -or $wc -eq $bc) {
            return $true
        }

        # Same diagonal: absolute row diff == absolute column diff
        if ([math]::Abs($wr - $br) -eq [math]::Abs($wc - $bc)) {
            return $true
        }

        return $false
    }

    [string]DrawBoard() {
        $rows = @()

        for ($r = 0; $r -lt 8; $r++) {
            $cells = @()
            for ($c = 0; $c -lt 8; $c++) {
                if ($this.White[0] -eq $r -and $this.White[1] -eq $c) {
                    $cells += 'W'
                }
                elseif ($this.Black[0] -eq $r -and $this.Black[1] -eq $c) {
                    $cells += 'B'
                }
                else {
                    $cells += '_'
                }
            }
            $rows += ($cells -join ' ')
        }

        # Tests expect CRLF line endings
        return ($rows -join "`r`n")
    }
}
