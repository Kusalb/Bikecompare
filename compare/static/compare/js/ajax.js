$(function () {
    $('#search').keyup(function () {
        $.ajax({
            type: "POST",
            url: "/compare/search/",
            data: {
                'search_text': $('#search').val()
            },
            success: function searchSuccess(data, textStatus, jqXHR)
            {
                console.log("test");
                $('#search-results').html(data)
            },
            dataType: 'html'
        });
    });
});

