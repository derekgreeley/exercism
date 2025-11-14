function Get-BobResponse {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, Position=0)]
        [AllowEmptyString()]
        [string]$HeyBob
    )

    process {
        # Silence: empty or only whitespace
        if ([string]::IsNullOrWhiteSpace($HeyBob)) {
            return "Fine. Be that way!"
        }

        # Trim only the end for question detection
        $trimmed    = $HeyBob.TrimEnd()
        $isQuestion = $trimmed.EndsWith('?')

        # Shouting: at least one letter, and NO lowercase letters (case-sensitive checks!)
        $hasLetters = $HeyBob -cmatch '[A-Za-z]'
        $isShouting = $hasLetters -and ($HeyBob -cmatch '[A-Z]') -and ($HeyBob -cnotmatch '[a-z]')

        if ($isShouting -and $isQuestion) {
            return "Calm down, I know what I'm doing!"
        }
        elseif ($isShouting) {
            return "Whoa, chill out!"
        }
        elseif ($isQuestion) {
            return "Sure."
        }
        else {
            return "Whatever."
        }
    }
}

