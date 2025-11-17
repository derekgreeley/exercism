function Get-SpaceAge {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position = 0)]
        [long]$Seconds,

        # Defaults to Earth if not provided
        [Parameter(Position = 1)]
        [string]$Planet = 'Earth'
    )

    # Seconds in one Earth year (given by the exercise)
    $earthYearSeconds = 31557600.0

    # Orbital period in Earth years for each planet
    $orbitalPeriods = @{
        Mercury = 0.2408467
        Venus   = 0.61519726
        Earth   = 1.0
        Mars    = 1.8808158
        Jupiter = 11.862615
        Saturn  = 29.447498
        Uranus  = 84.016846
        Neptune = 164.79132
    }

    # Normalize the planet name to match the keys above (e.g. "earth" -> "Earth")
    $normalizedPlanet =
        if ($Planet.Length -gt 0) {
            $Planet.Substring(0,1).ToUpper() + $Planet.Substring(1).ToLower()
        } else {
            'Earth'
        }

    if (-not $orbitalPeriods.ContainsKey($normalizedPlanet)) {
        throw "Invalid planet"
    }

    $period = $orbitalPeriods[$normalizedPlanet]

    # Age in planetary years
    $age = $Seconds / ($earthYearSeconds * $period)

    # Round to 2 decimal places to match expected test values
    [math]::Round($age, 2)
}
