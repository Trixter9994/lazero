import java.awt.AWTException;
// import java.awt.Desktop;
import java.awt.Dimension;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
// import java.io.File;
import java.io.IOException;
// import java.text.DateFormat;
// import java.text.SimpleDateFormat;
// // import java.util.*;
// java is shit.
// this is realy weird. all the things are doing against me.
// import javax.imageio.ImageIO;
// ain't you want to attach a process, read content, or in-memory process?
// first we have to digest the whole things. logic might be applied, but not so soon??
// import java.lang.reflect.*;
// import java.lang.Object.*;
// yes there are super functions inside. but we are creating the main package!
public class Mainshot {

    public static void main(String[] args) throws AWTException, IOException {
        // 获取屏幕的尺寸
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        System.out.println(
                "The width and the height of the screen are " + screenSize.getWidth() + " x " + screenSize.getHeight());
        // 截取屏幕
        BufferedImage image = new Robot().createScreenCapture(new Rectangle(screenSize));
        // System.out.println(image);
        // better broadcast the directory so we can access it! make it possible.
        // 设置日期格式，作为目录名
        // DateFormat dfDirectory = new SimpleDateFormat("yyyyMMdd");
        // System.out.println(dfDirectory);
        System.out.println(image);
        // 创建一个用于保存图片的文件夹
        // String st = "J:" + File.separator + "ScreenCapture" + File.separator + dfDirectory.format(new Date());
        // System.out.println(st);
        // File screenCaptureDirectory = new File(st);
        // if (!screenCaptureDirectory.exists()) {
            // screenCaptureDirectory.mkdirs();
            // System.out.println("The directory " + screenCaptureDirectory.getName() + " is created.");
        // } // get all things.
        // something is hard to realize, here is impossible.
// java 
        // // 设置日期格式，作为图片名
        // DateFormat dfImageName = new SimpleDateFormat("yyyyMMddhhmmss");
        // // 指定路径，并以特定的日期格式作为图片的名称
        // File imageFile = new File(screenCaptureDirectory, (dfImageName.format(new Date()) + ".png"));
        // Field[] field = File.class.getFields();
        // for (Field field2 : field) {
        //     System.out.println(field2);
        // }
        // Class f = Class.forName("java"+"io.File");
        // Class fx = File.class;
        // Method[] m0=fx.getDeclaredMethods();
        // for (Method m: m0){
        //     System.out.println(m);
        // }
        // really appreciate this.
        // i really think it is so verbose that even coding has became a serious problem.
        // so that's when you peruse.
        // not working.
        // List<Field> fl = Arrays.asList(field).stream().filter(field -> Modifier.isPublic(field.getModifiers()).collect(Collectors.toList()));
        // // 以指定的图片格式将截取的图片写到指定的文件
        // doesn't matter. if want to digress, do it in other location.
        // do not mess around the main codebase anymore.
        // wow, you finally have some sense on this computer, ain't you?
        // System.out.println(imageFile.getAbsolutePath());
        // ImageIO.write(image, "png", imageFile);
// no matter it is julia, python, java, it always sucks.
// and if... just if... knowing why it sucks...
        // // // 自动打开图片（没看懂！）
        // if (Desktop.isDesktopSupported() && Desktop.getDesktop().isSupported(Desktop.Action.OPEN)) {
        //     Desktop.getDesktop().open(imageFile);
        // }
    }
}