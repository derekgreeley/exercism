# Poker.ps1

function Get-BestHand {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string[]]$Hands
    )

    $scored = foreach ($hand in $Hands) {
        [pscustomobject]@{
            Hand  = $hand
            Score = Get-HandScoreString -Hand $hand
        }
    }

    $bestScore = ($scored | Sort-Object Score -Descending | Select-Object -First 1).Score

    # Preserve original order for ties
    $winners = foreach ($s in $scored) {
        if ($s.Score -eq $bestScore) { $s.Hand }
    }

    return @($winners)
}

function Get-HandScoreString {
    param([Parameter(Mandatory)][string]$Hand)

    $cards = $Hand -split '\s+' | Where-Object { $_ -ne '' }
    if ($cards.Count -ne 5) { throw "Invalid hand" }

    $vals = @()
    $suits = @()

    foreach ($c in $cards) {
        $suits += $c.Substring($c.Length - 1, 1)
        $r = $c.Substring(0, $c.Length - 1)

        $v = switch ($r) {
            'A'  { 14 }
            'K'  { 13 }
            'Q'  { 12 }
            'J'  { 11 }
            '10' { 10 }
            '9'  { 9 }
            '8'  { 8 }
            '7'  { 7 }
            '6'  { 6 }
            '5'  { 5 }
            '4'  { 4 }
            '3'  { 3 }
            '2'  { 2 }
            default { throw "Invalid rank" }
        }

        $vals += $v
    }

    $isFlush = (($suits | Select-Object -Unique).Count -eq 1)

    # Straight detection (incl. A-2-3-4-5)
    $unique = $vals | Sort-Object -Unique
    $isStraight = $false
    $straightHigh = 0
    if ($unique.Count -eq 5) {
        $sorted = $unique | Sort-Object
        if ($sorted[-1] - $sorted[0] -eq 4) {
            $isStraight = $true
            $straightHigh = $sorted[-1]
        }
        elseif (($sorted -join ',') -eq '2,3,4,5,14') {
            $isStraight = $true
            $straightHigh = 5
        }
    }

    # Group ranks by count, then by rank value
    $groups = $vals | Group-Object | ForEach-Object {
        [pscustomobject]@{ Value = [int]$_.Name; Count = $_.Count }
    } | Sort-Object -Property @{Expression='Count';Descending=$true}, @{Expression='Value';Descending=$true}

    # Build score vector: [Category, tiebreakers...]
    # Category: 8 SF, 7 4K, 6 FH, 5 F, 4 S, 3 3K, 2 2P, 1 1P, 0 HC
    $vec = @()

    if ($isStraight -and $isFlush) {
        $vec = @(8, $straightHigh)
    }
    elseif ($groups[0].Count -eq 4) {
        $quad = $groups[0].Value
        $kicker = ($groups | Where-Object Count -eq 1 | Select-Object -First 1).Value
        $vec = @(7, $quad, $kicker)
    }
    elseif ($groups[0].Count -eq 3 -and $groups[1].Count -eq 2) {
        $vec = @(6, $groups[0].Value, $groups[1].Value)
    }
    elseif ($isFlush) {
        $kickers = $vals | Sort-Object -Descending
        $vec = @(5) + @($kickers)
    }
    elseif ($isStraight) {
        $vec = @(4, $straightHigh)
    }
    elseif ($groups[0].Count -eq 3) {
        $trip = $groups[0].Value
        $kickers = ($groups | Where-Object Count -eq 1 | Select-Object -ExpandProperty Value) | Sort-Object -Descending
        $vec = @(3, $trip) + @($kickers)
    }
    elseif ($groups[0].Count -eq 2 -and $groups[1].Count -eq 2) {
        $pairHigh = [Math]::Max($groups[0].Value, $groups[1].Value)
        $pairLow  = [Math]::Min($groups[0].Value, $groups[1].Value)
        $kicker   = ($groups | Where-Object Count -eq 1 | Select-Object -First 1).Value
        $vec = @(2, $pairHigh, $pairLow, $kicker)
    }
    elseif ($groups[0].Count -eq 2) {
        $pair = $groups[0].Value
        $kickers = ($groups | Where-Object Count -eq 1 | Select-Object -ExpandProperty Value) | Sort-Object -Descending
        $vec = @(1, $pair) + @($kickers)
    }
    else {
        $high = $vals | Sort-Object -Descending
        $vec = @(0) + @($high)
    }

    # Convert to fixed-width sortable string (lexicographic works)
    # Pad each number to 2 digits; category is single-digit but pad anyway.
    return ($vec | ForEach-Object { '{0:D2}' -f $_ }) -join '-'
}
