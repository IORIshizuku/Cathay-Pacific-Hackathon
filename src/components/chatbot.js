$(document).ready(function () {
    $('.chat-input').on('keydown', function (e) {
        if (e.keyCode == 13 && $(this).val()) {  // Enter key pressed and input field is not empty
            const message = $(this).val();
            $(this).val('');
            $('.chat-output').append(`<p>You: ${message}</p>`);  // Display user's message
            
            $.ajax({
                url: '/run_script',
                type: 'POST',
                data: JSON.stringify({ 'query': message }),
                contentType: 'application/json;charset=UTF-8',
                success: function (response) {
                    $('.chat-output').append(`<p>Bot: ${response.response}</p>`);  // Display bot's response
                },
                error: function (error) {
                    console.error(error);
                }
            });
        }
    });
});