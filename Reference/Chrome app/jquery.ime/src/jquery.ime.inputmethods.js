( function ( $ ) {
	'use strict';

	// All keys have quotes for consistency
	/* eslint-disable quote-props */
	$.extend( $.ime.sources, {
		'or-inscript': {
			name: 'ଇନସ୍କ୍ରିପ୍ଟ',
			source: 'rules/or/or-inscript.js'
		},
		'or-inscript2': {
			name: 'ଇନସ୍କ୍ରିପ୍ଟ2',
			source: 'rules/or/or-inscript2.js'
		},
		'or-fasttype': {
			name: 'ଫାଷ୍ଟ୍‍ଟାଇପ୍',
			source: 'rules/or/or-fasttype.js'
		},
		'or-lekhani': {
			name: 'ଲେଖନୀ',
			source: 'rules/or/or-lekhani.js'
		},
		'or-OdiScript': {
			name: 'ଓଡ଼ିସ୍କ୍ରିପ୍ଟ',
			source: 'rules/or/or-OdiScript.js'
		},
		'or-phonetic': {
			name: 'ଫୋନେଟିକ',
			source: 'rules/or/or-phonetic.js'
		},
		'or-transliteration': {
			name: 'ଟ୍ରାନ୍ସଲିଟରେସନ',
			source: 'rules/or/or-transliteration.js'
		}
	} );
	/* eslint-disable quote-props */

	$.extend( $.ime.languages, {
		
		or: {
			autonym: 'ଓଡ଼ିଆ',
			inputmethods: [ 'or-fasttype', 'or-phonetic', 'or-transliteration', 'or-inscript', 'or-inscript2', 'or-lekhani', 'or-OdiScript' ]
		}
	} );

}( jQuery ) );
