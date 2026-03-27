class Allergies {
    [int]$Score
    [hashtable]$AllergenMap

    Allergies([int]$score) {
        $this.Score = $score

        $this.AllergenMap = @{
            "eggs" = 1
            "peanuts" = 2
            "shellfish" = 4
            "strawberries" = 8
            "tomatoes" = 16
            "chocolate" = 32
            "pollen" = 64
            "cats" = 128
        }
    }

    [bool] IsAllergicTo([string]$allergen) {
        if (-not $this.AllergenMap.ContainsKey($allergen)) {
            return $false
        }

        $value = $this.AllergenMap[$allergen]

        return (($this.Score -band $value) -ne 0)
    }

    [string[]] GetAllergies() {
        $result = @()

        foreach ($key in @(
            "eggs", "peanuts", "shellfish", "strawberries",
            "tomatoes", "chocolate", "pollen", "cats"
        )) {
            if ($this.IsAllergicTo($key)) {
                $result += $key
            }
        }

        return $result
    }
}