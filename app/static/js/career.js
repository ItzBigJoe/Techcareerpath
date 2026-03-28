document.addEventListener("DOMContentLoaded", function () {

  fetch('/api/result')  // 🔥 Better endpoint than /api/submit
    .then(res => res.json())
    .then(data => {

      // Career + Score
      document.getElementById("career-title").textContent = data.career;
      document.getElementById("score-value").textContent = data.score + "%";
      document.getElementById("score-bar").style.width = data.score + "%";

      // Split skills into categories
      let techHTML = "";
      let softHTML = "";
      let metricsHTML = "";

      for (let skill in data.skills) {
        if (skill === "Readiness") continue; // Skip overall readiness
        
        let value = data.skills[skill];

        let block = `
          <div class="skill-row">
            <p>${skill} <span>${value}%</span></p>
            <div class="progress-bar">
              <div class="progress" style="width:${value}%"></div>
            </div>
          </div>
        `;

        // Classification logic
        const techCategories = ["Frontend", "Backend", "AI/Data Science", "DSA"];
        const metricsCategories = ["Domain Fit", "Tag Similarity"];
        
        if (techCategories.includes(skill)) {
          techHTML += block;
        } else if (skill === "Soft Skills") {
          softHTML += block;
        } else if (metricsCategories.includes(skill)) {
          metricsHTML += block;
        }
      }

      document.getElementById("technical-skills").innerHTML = techHTML;
      document.getElementById("soft-skills").innerHTML = softHTML;
      
      // Inject metrics if we have a container (we might need to add it to career.html)
      const metricsContainer = document.getElementById("advanced-metrics");
      if (metricsContainer) {
        metricsContainer.innerHTML = metricsHTML;
      }

      // Advanced Gaps (Task 8)
      let gapHTML = "";
      if (data.gaps.missing && data.gaps.missing.length > 0) {
        gapHTML += `<li style="font-weight: bold; color: #c62828;">Critical Missing Skills:</li>`;
        data.gaps.missing.forEach(g => {
          gapHTML += `<li>❌ ${g}</li>`;
        });
      }
      
      if (data.gaps.weak && data.gaps.weak.length > 0) {
        gapHTML += `<li style="font-weight: bold; color: #f9a825; margin-top: 10px;">Skills to Improve:</li>`;
        data.gaps.weak.forEach(g => {
          gapHTML += `<li>⚠️ ${g}</li>`;
        });
      }

      document.getElementById("gap-list").innerHTML = gapHTML || "<li>No major skill gaps identified! You are well-prepared.</li>";

    })
    .catch(err => {
      console.error(err);
      document.getElementById("career-title").textContent = "Error loading result";
    });

});