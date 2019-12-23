$(function(){
			$('#search').keyup(function(){

				$.ajax({
					type:"POST",
					url:"search_console",
					data: {
						'search_text' : $('#search').val(),
						'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()

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




$(function(){
				$('#searchsong').keyup(function(){
	
					$.ajax({
						type:"POST",
						url:"/guitar/search_consoles",
						data: {
							'search_text' : $('#searchsong').val(),
							'csrfmiddlewaretoken' : $('input[name=csrfmiddlewaretoken]').val()
	
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
	