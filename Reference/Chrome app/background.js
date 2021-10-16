chrome.app.runtime.onLaunched.addListener(function() {
  chrome.app.window.create('jquery.ime/root/index.html', {
    'outerBounds': {
      'width': 400,
      'height': 500
    }
  });
});