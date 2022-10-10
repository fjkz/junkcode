package fjk.jobrunr;

import org.jobrunr.jobs.JobId;
import org.jobrunr.scheduling.JobScheduler;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/job")
public class JobController {
    private final JobScheduler jobScheduler;

    public JobController(JobScheduler jobScheduler) {
        this.jobScheduler = jobScheduler;
    }

    @GetMapping(value = "/hello", produces = {MediaType.TEXT_PLAIN_VALUE})
    public String simpleJob(@RequestParam(value = "name", defaultValue = "World") String name) {
        final JobId enqueuedJobId = this.jobScheduler.enqueue(() -> System.out.println("Hello World"));
        return "Job Enqueued: " + enqueuedJobId;
    }
}
