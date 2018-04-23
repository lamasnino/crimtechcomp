function alphanumeric(inputtxt){ 
	var letters = /^[0-9a-zA-Z]+$/;
	if(inputtxt.value.match(letters))
		{
			return true;
		}
		else
			{
				return false;
			}
		}


function encode(msg,key) {
	var key_count = 0;
	var alphabet ='abcdefghijklmnopqrstuvwxyz';
	var length_key = key.length;
	var result = "";
	var _switch = true;
	var x;

	for (x in msg) {
		if(_switch){
			var key_character = key[key_character];
			if (alphanumeric(key_character)){
				var encoded_number = alphabet.indexOf(encoded_number)+alphabet.indexOf(key_character)+1;
				result += 

			}
		}
	}


	return result;
}

