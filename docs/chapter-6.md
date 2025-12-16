📘 **CHAPTER 6 – Capstone: Autonomous Humanoid Robot**

### **SLIDE 1 – Chapter Title**

**Capstone Project**
**Chapter 6: Autonomous Humanoid Robot**

Bringing all robotics and AI components together.

---

### **SLIDE 2 – Chapter Overview**

**What You Will Learn**

* How all modules integrate into one system
* End-to-end autonomous robot workflow
* Sim-to-real deployment
* Real-world humanoid task execution

This chapter represents the final practical application.

---

### **SLIDE 3 – Introduction to Capstone Project**

The **Capstone Project** focuses on:

* Integration of perception, planning, and control
* Combining AI, ROS 2, simulation, and hardware

**Goal:**
Robot understands commands, navigates, and manipulates objects autonomously.

---

### **SLIDE 4 – Overall System Architecture**

The autonomous humanoid system consists of:

* Training & simulation environment
* Onboard AI computation
* Sensors and actuators

Each component plays a critical role.

---

### **SLIDE 5 – Compute & Control Units**

**Workstation**

* Trains AI models
* Runs Isaac Sim and simulations

**Edge Brain (Jetson)**

* Deploys trained AI models
* Executes real-time decisions on robot

---

### **SLIDE 6 – Sensors & Actuators**

**Sensors**

* Intel RealSense Camera – Vision
* LiDAR – Mapping & navigation
* IMU – Balance & orientation

**Actuators**

* Unitree Go2 / G1 humanoid platform

---

### **SLIDE 7 – Sim-to-Real Workflow**

End-to-end workflow:

* Train robot in **Isaac Sim**
* Generate AI policies
* Deploy models on **Jetson**
* Execute commands on physical robot

This reduces risk and improves reliability.

---

### **SLIDE 8 – Why Sim-to-Real Matters**

Sim-to-real transfer:

* Saves development time
* Reduces hardware damage
* Improves real-world performance

Simulation prepares robots for reality.

---

### **SLIDE 9 – Example: Autonomous Task**

**Voice Command:**
“Pick up red block and place on shelf”

The robot must interpret, plan, and execute autonomously.

---

### **SLIDE 10 – Robot Task Planning**

**Robot Plan:**

* Navigate to the block
* Detect and identify red block
* Grasp the object
* Move to shelf location
* Release the block

This shows multi-step autonomy.

---

### **SLIDE 11 – Technologies Integrated**

The capstone integrates:

* ROS 2 communication
* Simulation (Isaac Sim)
* NVIDIA Isaac ROS
* Vision-Language-Action (VLA)
* Real robot hardware

This demonstrates full-stack robotics.

---

### **SLIDE 12 – Chapter Summary**

* Capstone project proves practical learning
* Integrates AI, simulation, and hardware
* Demonstrates autonomous humanoid behavior
* Represents real-world robotics deployment
