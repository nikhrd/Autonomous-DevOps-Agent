import InputSection
from "./components/InputSection";

import Dashboard
from "./components/Dashboard";

export default function App() {

  return (

    <div
      className="
      p-6
      max-w-7xl
      mx-auto"
    >

      <h1
        className="
        text-4xl
        font-bold
        mb-6"
      >
        Autonomous DevOps Agent
      </h1>

      <InputSection />

      <div
        className="mt-6"
      >

        <Dashboard />

      </div>

    </div>
  );
}