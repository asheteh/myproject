	$(function(){
			$('#search').keyup(function(){

				$.ajax({
					type:"POST",
					url:'music',
					data: {
						'search_text' : $('#search').val(),
						'csrfmiddlerwaretoken' : $('input[name=csrfmiddlerwaretoken]').val()

					},
					success:searchSuccess,
					dataType :'html'
				});
			});

		});
			function searchSuccess(data,textStatus,jqXHR)
			{
				$('#search-results').html(data);
			}