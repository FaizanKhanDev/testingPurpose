$('#show-more-content').hide();

$('#show-more').click(function() {
  $('#show-more-content').show();
  $('#show-less').show();
  $(this).hide();
});

$('#show-less').click(function() {
  $('#show-more-content').hide();
  $('#show-more').show();
  $(this).hide();

  $("#show-more")[0].scrollIntoView();
});