function submitComment(event) {
    event.preventDefault(); // Prevent form submission

    // Get the user's comment from the input field
    var commentInput = document.getElementById("commentInput");
    var commentText = commentInput.value;

    // Create a new list item for the comment
    var newComment = document.createElement("li");
    newComment.className = "comment";
    newComment.innerHTML = `
        <div class="comment-user">
            <img src="../src/components/images/user_icon.jpeg" alt="User Icon" class="user-icon me-2" style="width: 30px; height: 30px; border-radius: 50%;">
            <strong>Franklin Poon</strong>
        </div>
        <p class="comment-text">${commentText}</p>
    `;

    // Add the new comment to the comments list
    var commentList = document.getElementById("commentList");
    commentList.appendChild(newComment);

    // Clear the comment input field
    commentInput.value = "";
}

document.getElementById('viewPostButton').addEventListener('click', function() {
    window.location.href = 'user123.html';
});

