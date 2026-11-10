
class SimpleCipher {

    [string]$_key

    # Constructor: Generate a random key
    SimpleCipher() {

        $alphabet = "abcdefghijklmnopqrstuvwxyz"
        $randomKey = [System.Text.StringBuilder]::new()

        # Generate 100 random lowercase letters
        for ($i = 0; $i -lt 100; $i++) {
            $index = Get-Random -Minimum 0 -Maximum 26
            [void]$randomKey.Append($alphabet[$index])
        }

        $this._key = $randomKey.ToString()
    }

    # Constructor: Use a supplied key
    SimpleCipher([string]$key) {

        if ([string]::IsNullOrEmpty($key) -or
            $key -cnotmatch '^[a-z]+$') {
            throw "Key must contain only lowercase letters."
        }

        $this._key = $key
    }

    # Encode plaintext into ciphertext
    [string] Encode([string]$text) {

        $result = [System.Text.StringBuilder]::new()

        for ($i = 0; $i -lt $text.Length; $i++) {

            # Convert plaintext character to 0-25
            $letter = [int]$text[$i] - [int][char]'a'

            # Repeat the key when necessary
            $keyIndex = $i % $this._key.Length

            # Convert key character to shift value
            $shift = [int]$this._key[$keyIndex] - [int][char]'a'

            # Shift forward and wrap around alphabet
            $encoded = ($letter + $shift) % 26

            # Convert number back to character
            $character = [char]($encoded + [int][char]'a')

            [void]$result.Append($character)
        }

        return $result.ToString()
    }

    # Decode ciphertext into plaintext
    [string] Decode([string]$text) {

        $result = [System.Text.StringBuilder]::new()

        for ($i = 0; $i -lt $text.Length; $i++) {

            # Convert ciphertext character to 0-25
            $letter = [int]$text[$i] - [int][char]'a'

            # Repeat the key when necessary
            $keyIndex = $i % $this._key.Length

            # Convert key character to shift value
            $shift = [int]$this._key[$keyIndex] - [int][char]'a'

            # Shift backward and wrap around alphabet
            $decoded = ($letter - $shift + 26) % 26

            # Convert number back to character
            $character = [char]($decoded + [int][char]'a')

            [void]$result.Append($character)
        }

        return $result.ToString()
    }
}
