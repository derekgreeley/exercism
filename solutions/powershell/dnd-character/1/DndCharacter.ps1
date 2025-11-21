class Character {
    [int]$Strength
    [int]$Dexterity
    [int]$Constitution
    [int]$Intelligence
    [int]$Wisdom
    [int]$Charisma
    [int]$HitPoints

    Character() {
        # Each ability is rolled once and cached on the instance
        $this.Strength     = $this.Ability()
        $this.Dexterity    = $this.Ability()
        $this.Constitution = $this.Ability()
        $this.Intelligence = $this.Ability()
        $this.Wisdom       = $this.Ability()
        $this.Charisma     = $this.Ability()

        # Hit points = 10 + constitution modifier
        $this.HitPoints = 10 + [Character]::GetModifier($this.Constitution)
    }

    static [int] GetModifier([int]$score) {
        # Modifier = floor((score - 10) / 2)
        return [int][math]::Floor(($score - 10) / 2)
    }

    [int] Ability() {
        # Roll 4d6, drop the lowest die, sum the highest three
        $rolls = @()
        1..4 | ForEach-Object {
            $rolls += Get-Random -Minimum 1 -Maximum 7  # 1–6 inclusive
        }

        $sorted = $rolls | Sort-Object
        $top3   = $sorted[1..3]  # drop the smallest (index 0)
        return ($top3 | Measure-Object -Sum).Sum
    }
}
