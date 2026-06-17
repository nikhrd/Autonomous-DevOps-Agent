import {
  VerticalTimeline,
  VerticalTimelineElement
}from "react-vertical-timeline-component";

import
"react-vertical-timeline-component/style.min.css";

interface Props {
  runs: any[];
}

export default function CICDTimeline({
  runs
}: Props) {

  return (
    <VerticalTimeline>

      {runs?.map(
        (
          run,
          index
        ) => (

          <VerticalTimelineElement
            key={index}
            title={
              run.status
            }
          >

            Iteration:
            {run.iteration}

            <br/>

            {run.timestamp}

          </VerticalTimelineElement>

        )
      )}

    </VerticalTimeline>
  );
}