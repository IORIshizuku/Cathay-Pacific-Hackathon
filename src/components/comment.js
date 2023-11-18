function submitComment(event) {
    event.preventDefault();

    var commentInput = document.getElementById("commentInput");
    var commentText = commentInput.value;

    var newComment = document.createElement("li");
    newComment.className = "comment";
    newComment.innerHTML = `
        <div class="comment-user">
            <img src="../src/components/images/user_icon.jpeg" alt="User Icon" class="user-icon me-2" style="width: 30px; height: 30px; border-radius: 50%;">
            <strong>Franklin Poon</strong>
        </div>
        <p class="comment-text">${commentText}</p>
    `;

    var commentList = document.getElementById("commentList");
    commentList.appendChild(newComment);

    commentInput.value = "";
}

document.getElementById('viewPostButton').addEventListener('click', function() {
    window.location.href = 'user123.html';
});

