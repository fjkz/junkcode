package fjk.jobrunr;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;

@SpringBootApplication
@Import(JobrunrStorageConfiguration.class)
public class JobrunrApplication {

	public static void main(String[] args) {
		SpringApplication.run(JobrunrApplication.class, args);
	}

}
