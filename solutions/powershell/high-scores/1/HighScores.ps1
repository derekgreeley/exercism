# HighScores.ps1

class HighScores {
    hidden [int[]] $Scores

    HighScores([int[]] $scores) {
        # Store a copy so callers can't mutate internal state via reference tricks
        $this.Scores = @($scores)
    }

    [int[]] GetScores() {
        # Return a copy (tests expect the same values, not the same array instance)
        return @($this.Scores)
    }

    [int] GetLatest() {
        return $this.Scores[$this.Scores.Length - 1]
    }

    [int] GetPersonalBest() {
        # Measure-Object returns an object; grab the Maximum property
        return ($this.Scores | Measure-Object -Maximum).Maximum
    }

    [int[]] GetTopThree() {
        # Sort descending, take up to 3, return as int[]
        $top = $this.Scores | Sort-Object -Descending | Select-Object -First 3
        return @($top)
    }
}
