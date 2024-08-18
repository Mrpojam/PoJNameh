const likeButtons = document.querySelectorAll('.like');
const dislikeButtons = document.querySelectorAll('.dislike');

likeButtons.forEach(button => {
    button.addEventListener('click', () => {
        alert('Liked!');
    });
});

dislikeButtons.forEach(button => {
    button.addEventListener('click', () => {
        alert('Disliked!');
    });
});
