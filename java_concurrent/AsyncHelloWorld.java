import java.util.concurrent.CompletableFuture;
	
class AsyncHelloWorld {
  public static void main(String[] args) throws Exception {
    for (int i = 0; i < 1000; i++) {
      final int world_num = i;
      CompletableFuture.runAsync(() -> {
	try {
          Thread.sleep(1000);
	} catch (InterruptedException e) {
	}
	var tname = Thread.currentThread().getName();
        System.out.println("Hello World #" + world_num + " from thread " + tname);
      });
    }
    Thread.sleep(100000);
  }
}
