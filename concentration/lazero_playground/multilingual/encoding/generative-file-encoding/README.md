# generative-file-encoding (PROTOTYPE FINISHED)
creates unique memory optimized encoded system per inputted files.


    import { gfe } from './main';
    let file0 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
    let bitspace = 6; // 2**6; // however much memory you want encoded
    console.log(
        gfe(file0, 6)
    );

