# PhoneNumber.ps1

function Get-PhoneNumber {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Number,

        [switch]$Pretty
    )

    begin {
        Set-StrictMode -Version Latest
        $PSDefaultParameterValues['*:ErrorAction'] = 'Stop'
    }

    process {
        # 1. Letters are never allowed
        if ($Number -match '[A-Za-z]') {
            throw "Letters not permitted"
        }

        # 2. Only allow digits, whitespace, ., -, (), and + as punctuation
        # Anything else non-digit is invalid punctuation
        if ($Number -match '[^0-9\+\-\.\(\)\s]') {
            throw "Punctuations not permitted"
        }

        # 3. Strip all non-digits
        $digits = $Number -replace '\D', ''

        # 4. Length checks
        if ($digits.Length -lt 10) {
            throw "Number can't be fewer than 10 digits"
        }
        elseif ($digits.Length -gt 11) {
            throw "Number can't be more than 11 digits"
        }
        elseif ($digits.Length -eq 11) {
            # Must start with country code '1'
            if ($digits[0] -ne '1') {
                throw "11 digits must start with 1"
            }
            # Drop the leading country code
            $digits = $digits.Substring(1)
        }

        # At this point we must have exactly 10 digits
        # 5. Area code validation (first digit)
        $areaFirst = $digits[0]
        if ($areaFirst -eq '0') {
            throw "Area code can't start with 0"
        }
        elseif ($areaFirst -eq '1') {
            throw "Area code can't start with 1"
        }

        # 6. Exchange code validation (fourth digit, index 3)
        $exchangeFirst = $digits[3]
        if ($exchangeFirst -eq '0') {
            throw "Exchange code can't start with 0"
        }
        elseif ($exchangeFirst -eq '1') {
            throw "Exchange code can't start with 1"
        }

        # 7. Return either raw or pretty-printed
        if ($Pretty) {
            $area     = $digits.Substring(0,3)
            $exchange = $digits.Substring(3,3)
            $subscriber = $digits.Substring(6,4)
            return "({0})-{1}-{2}" -f $area, $exchange, $subscriber
        }
        else {
            return $digits
        }
    }
}
