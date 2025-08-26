package havefun.goodluck;

import java.lang.reflect.*;
import java.nio.charset.StandardCharsets;
import java.util.HexFormat;
import java.util.Locale;

public class Main {

    public static byte[] goldenticket = HexFormat.of()
            .parseHex("aeaf98ccb0b1ced8b3fe8fdfbfe7cac3bafa959eadfb9ad0");

    @SuppressWarnings("UseSpecificCatch")
    public static void main(String[] args) {
        System.out.println("--- CAFE1995 AUTHENTICATION SYSTEM - BETA ---");

        try {
            Class<Main> nameofvariable1242151251 = Main.class;
            Main hereiswhereweinitializemain = new Main();
            if (args.length == 0) {
                System.out.println("HELP: Enter a <password> and <method name> as arguments.");
                System.out.println("NOTICE: AUTHORISED PERSONS ONLY.");
                System.out.println();
                System.out.println("=== Starting Java Method Reflection Utility === Copyright (c) 1995  John Doe ===");
                System.out.println("This software is not activated. For improved security, please specify your license key.");
                System.out.println("=== End Trial License Notice ===");
                System.out.println();
                System.out.println("> METHODS AVAILABLE:");
                for (final Method clazz : nameofvariable1242151251.getDeclaredMethods()) {
                    System.out.println(" -> " + clazz.getName());
                }
                System.out.println("NOTICE: Some methods do not check authentication yet, please proceed with caution!");
                System.out.println("Furthermore, the program is still work in progress, only 3 of these methods will be useful. And don't you dare try to get the password!");
                System.out.println("NO DOCUMENTATION PROVIDED. THIS CODE IS SELF-DOCUMENTING.");
            } else if (args.length == 1 || args.length == 2) {
                String jvmBytecodeToExecute = args[0].toLowerCase(Locale.ROOT);
                if (jvmBytecodeToExecute.startsWith("0x")) {
                    jvmBytecodeToExecute = jvmBytecodeToExecute.substring(2);
                }
                byte[] michaelsoft = HexFormat.of().parseHex(jvmBytecodeToExecute);
                String keyinput = args[1];
                Method javavirtualmachine = nameofvariable1242151251.getMethod(keyinput, byte[].class, byte[].class);
                System.out.println("> REQUEST OK... QUERYING SYSTEM...");
                byte[] spaghetti = (byte[]) javavirtualmachine.invoke(hereiswhereweinitializemain, michaelsoft, goldenticket);
                System.out.println("> QUERY SUCCESS");
                System.out.println("rawBytes = " + HexFormat.of().formatHex(spaghetti));
                System.out.println("asString = " + new String(spaghetti, StandardCharsets.UTF_8));
            }
        } catch (Exception ignored) {
            System.out.println("MALFUNCTION;");
        }
        System.out.println("--- Terminating program ---");
    }

    @SuppressWarnings("unused")
    public byte[] passwordHint(byte[] printstatement, byte[] somebytearray) {
        System.out.println("Passwords are numeric only, it's all our punch card system can handle.");
        System.out.println("Did you hear how much hard drives used to cost?");
        System.out.println("Some employees speak in common Hex phrases to make it easier to remember.");
        System.out.println("Due to database limitations, one of the characters is reserved for internal use and " +
                "cannot be used in the password.");
        System.out.println("Closed source program, sorry - security through obscurity!");
        byte[] c = new byte[somebytearray.length];
        for (int i = 0; i < somebytearray.length; i++) {
            c[i] = (byte) (somebytearray[i] + 3);
        }
        return helloworld(printstatement, c, false);
    }

    @SuppressWarnings("unused")
    public byte[] flag(byte[] goodbyedecompiler1, byte[] hellodecompiler5) {
        System.out.println("You do not have access to this method. This has been reported to the administrator.");
        byte[] goodbyedecompiler2 = new byte[hellodecompiler5.length];
        for (int goodbyedecompiler3 = 0; goodbyedecompiler3 < hellodecompiler5.length; goodbyedecompiler3++) {
            goodbyedecompiler2[goodbyedecompiler3] = (byte) (hellodecompiler5[goodbyedecompiler3] << 1);
        }
        return set(goodbyedecompiler1, helloworld(hellodecompiler5, goodbyedecompiler2, true));
    }

    public byte[] set(byte[] hellodecompiler1, byte[] hellodecompiler2) {
        byte[] hellodecompiler3 = new byte[hellodecompiler2.length];
        for (int hellodecompiler4 = 0; hellodecompiler4 < hellodecompiler3.length; hellodecompiler4++) {
            hellodecompiler3[hellodecompiler4] = (byte) ((hellodecompiler2[0] == 0xB && hellodecompiler2[1] == 0xA) ?
                    (hellodecompiler2[hellodecompiler4] << 2) :
                    hellodecompiler2[hellodecompiler4] + 3);
        }
        System.setProperty("E375931538A853FF", "0x1");
        return get(hellodecompiler1, hellodecompiler3);
    }

    public byte[] get(byte[] jack, byte[] wendy) {
        byte[] donald = new byte[wendy.length];
        for (int kentucky = 0; kentucky < donald.length; kentucky++) {
            donald[kentucky] = (byte) ((wendy[0] == 0xB && wendy[1] == 0xA) ?
                    (wendy[kentucky] << 2) :
                    wendy[kentucky] - 3);
        }
        return helloworld(jack, donald, false);
    }

    @SuppressWarnings("unused")
    public byte[] build1(byte[] mate, byte[] notmate) {
        byte[] spinach = new byte[notmate.length];
        for (int totallynotspinach = 0; totallynotspinach < notmate.length; totallynotspinach++) {
            spinach[totallynotspinach] = (byte) (notmate[totallynotspinach] >> 2);
        }
        return helloworld(mate, spinach, System.getProperty("E375931538A853FF").equals("0x1"));
    }

    @SuppressWarnings("unused")
    public byte[] build2(byte[] amplifier, byte[] strat) {
        System.out.println("//Note to self: Had a coffee this morning.");
        System.out.println("Tasted rather... bad... changed the beans and all, just why??");
        System.out.println("Go to the other cafe. Make sure to hit Tony's new lines of code KPI.");
        System.out.println("Don't bother with documentation.");
        System.out.println("//FIXME: Remove this comment before shipping the new secure auth system!!");
        byte[] cord = new byte[strat.length];
        for (int pedal = 0; pedal < strat.length; pedal++) {
            cord[pedal] = (byte) (strat[pedal] - 3);
        }
        return helloworld(amplifier, cord, false);
    }

    private byte[] helloworld(byte[] jen, byte[] craig, boolean sam) {
        byte[] bowl = new byte[craig.length];
        for (int spoon = 0; spoon < bowl.length; spoon++) {
            bowl[spoon] = sam ? (byte) (craig[spoon] ^ jen[spoon % jen.length] << 2) : (byte) (craig[spoon] ^ jen[spoon % jen.length]);
        }
        return bowl;
    }
}
