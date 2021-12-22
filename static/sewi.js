function readImage(path) {
    if (!path) return null;
    let resolve = null;
    const rtn = new Promise((r) => {
        resolve = r;
    });
    const reader = new FileReader();
    reader.addEventListener('load', (e) => {
        resolve(e.target.result);
    });
    reader.readAsDataURL(path);
    return rtn;
}

document.addEventListener('DOMContentLoaded', (event) => {
    const input = document.querySelector("#file-input");
    input.addEventListener('change', async (event) => {
        const image = await readImage(event.target.files[0]);
        console.log(image);
        axios.post('/picture/upload', { image });
    });
});
