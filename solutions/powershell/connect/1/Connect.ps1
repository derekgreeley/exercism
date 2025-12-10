Set-StrictMode -Version Latest

enum Winner {
    NONE
    X
    O
}

class Connect {
    [char[,]] $Grid
    [int]     $Rows
    [int]     $Cols

    Connect([string[]] $boardLines) {
        if (-not $boardLines -or $boardLines.Count -eq 0) {
            throw "Board must contain at least one row."
        }

        $this.Rows = $boardLines.Count

        # Parse first row to determine column count
        $firstTokens = $boardLines[0].Trim().Split(' ', [System.StringSplitOptions]::RemoveEmptyEntries)
        $this.Cols = $firstTokens.Count

        $this.Grid = New-Object 'char[,]' $this.Rows, $this.Cols

        for ($r = 0; $r -lt $this.Rows; $r++) {
            $tokens = $boardLines[$r].Trim().Split(' ', [System.StringSplitOptions]::RemoveEmptyEntries)

            if ($tokens.Count -ne $this.Cols) {
                throw "All rows must have the same number of columns."
            }

            for ($c = 0; $c -lt $this.Cols; $c++) {
                $this.Grid[$r, $c] = [char]$tokens[$c]
            }
        }
    }

    [Winner] GetWinner() {
        if ($this.HasPath('X')) {
            return [Winner]::X
        }
        if ($this.HasPath('O')) {
            return [Winner]::O
        }
        return [Winner]::NONE
    }

    hidden [bool] HasPath([char] $player) {
        # Neighbor offsets for hex adjacency in this skewed grid
        $neighbors = @(
            @{ dr = -1; dc =  0 },
            @{ dr = -1; dc =  1 },
            @{ dr =  0; dc = -1 },
            @{ dr =  0; dc =  1 },
            @{ dr =  1; dc = -1 },
            @{ dr =  1; dc =  0 }
        )

        $visited = New-Object 'bool[,]' $this.Rows, $this.Cols
        $stack   = New-Object 'System.Collections.Generic.Stack[object]'

        if ($player -eq 'X') {
            # X connects left (col 0) to right (col Cols-1)
            for ($r = 0; $r -lt $this.Rows; $r++) {
                if ($this.Grid[$r,0] -eq 'X') {
                    $stack.Push(@($r,0))
                    $visited[$r,0] = $true
                }
            }
            while ($stack.Count -gt 0) {
                $pos = $stack.Pop()
                $r = $pos[0]
                $c = $pos[1]

                if ($c -eq ($this.Cols - 1)) {
                    return $true
                }

                foreach ($n in $neighbors) {
                    $nr = $r + $n.dr
                    $nc = $c + $n.dc
                    if ($nr -ge 0 -and $nr -lt $this.Rows -and
                        $nc -ge 0 -and $nc -lt $this.Cols -and
                        -not $visited[$nr,$nc] -and
                        $this.Grid[$nr,$nc] -eq 'X') {

                        $visited[$nr,$nc] = $true
                        $stack.Push(@($nr,$nc))
                    }
                }
            }
            return $false
        }
        elseif ($player -eq 'O') {
            # O connects top (row 0) to bottom (row Rows-1)
            for ($c = 0; $c -lt $this.Cols; $c++) {
                if ($this.Grid[0,$c] -eq 'O') {
                    $stack.Push(@(0,$c))
                    $visited[0,$c] = $true
                }
            }
            while ($stack.Count -gt 0) {
                $pos = $stack.Pop()
                $r = $pos[0]
                $c = $pos[1]

                if ($r -eq ($this.Rows - 1)) {
                    return $true
                }

                foreach ($n in $neighbors) {
                    $nr = $r + $n.dr
                    $nc = $c + $n.dc
                    if ($nr -ge 0 -and $nr -lt $this.Rows -and
                        $nc -ge 0 -and $nc -lt $this.Cols -and
                        -not $visited[$nr,$nc] -and
                        $this.Grid[$nr,$nc] -eq 'O') {

                        $visited[$nr,$nc] = $true
                        $stack.Push(@($nr,$nc))
                    }
                }
            }
            return $false
        }
        else {
            return $false
        }
    }
}
