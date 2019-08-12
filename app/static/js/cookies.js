// возвращает cookie если есть или undefined
function getCookie(name) {

	var matches = document.cookie.match(new RegExp(
	  "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
	))
	return matches ? decodeURIComponent(matches[1]) : undefined
}

// уcтанавливает cookie
function setCookie(name, value, options = {}) {

  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
	updatedCookie += "; " + optionKey;
	let optionValue = options[optionKey];
	if (optionValue !== true) {
	  updatedCookie += "=" + optionValue;
	}
  }

  document.cookie = updatedCookie;
}

// удаляет cookie
function deleteCookie(name) {

	setCookie(name, null, { expires: -1 })

}